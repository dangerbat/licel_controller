#!/usr/bin/python3
import asyncio
from multiprocessing import Pool
from licel_controller import HOST, PORT, tr_commands


class Controller():
    def __init__(self, *args, **kwargs):
        self.commands_to_execute = []

    def run(self):
        with Pool(1) as pool:
            try:
                pool.map(client, self.commands_to_execute)
            except OSError:
                print("Connection failed..")

    def crlf(self):
        return "\r\n"

    def to_bytes(self, command):
        return command.encode()

    def add(self, command):
        self.commands_to_execute.append(
            self.to_bytes(command)
        )

    def select(self, *devices):
        transient_recorders = ', '.join(str(device) for device in devices)
        command = tr_commands.SELECT + " " + transient_recorders + self.crlf()
        self.add(command)

    def pmtgain(self, device, voltage):
        command = tr_commands.PMTGAIN + " " + str(device) \
                  + " " + str(voltage) + self.crlf()
        self.add(command)

    def mstart(self):
        command = tr_commands.MSTART + self.crlf()
        self.add(command)

    def mstop(self):
        command = tr_commands.MSTOP + self.crlf()
        self.add(command)


def client(command):

    @asyncio.coroutine
    def tcp_echo_client(loop):
        reader, writer = yield from asyncio.open_connection(
            HOST, PORT, loop=loop)
        print(f'Send: {command.decode()!r}')
        writer.write(command)
        data = yield from reader.readline()
        print("Client received {!r} from server".format(data))
        writer.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tcp_echo_client(loop))
