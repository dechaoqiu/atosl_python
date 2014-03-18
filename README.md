atosl
=====

atosl: atosl is short for atos for linux. It is partial replacement for Mac OS X's atos tool which can be used for converting macho binary addresses into symbols. This version does not depend on any existing library. 

I wrote this tool when I was developing http://egg.io with my friends, and we can not find a usable atos tool for our Linux server. So we decided to develop our own atos. And we use atosl instead of atos to avoid conflict with apple's existing atos tool. In order to avoid reinventing wheels we decide to make it open source.

sample macho file can be reached at https://github.com/renoqiu/atosl/tree/master/test/res

## INSTALL

1. pip install atosl

## USAGE

    import atosl
    atosl.symbolicate(arch_str, macho_path, addresses_tuple)

## EXAMPLE

1. atosl.symbolicate('armv7s', 'test/res/CrashTest3Dwarf.fat', ("0x00006ed7", ))

