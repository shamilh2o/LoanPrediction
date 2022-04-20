from h2o_wave import ui

'''
-------------------------------------------------------------------------------
header
-------------------------------------------------------------------------------
title      20|80 commands_top
-------------------------------------------------------------------------------
                                    commands
-------------------------------------------------------------------------------
content --------
                              50|50 main
                        ---------
main left                       |   main_right
                                |
                                |   
                                |
                                |
-------------------------------------------------------------------------------
                            main_center
-------------------------------------------------------------------------------
footer
-------------------------------------------------------------------------------
'''


def get_layouts():
    layouts = [
        ui.layout(
            breakpoint='xl',
            width='calc(100vw)',
            height='calc(100vh)',
            max_height='calc(100vh)',
            zones=[
                ui.zone('header'),
                ui.zone(
                    'title_commands',
                    direction=ui.ZoneDirection.ROW,
                    zones=[
                        ui.zone('title', size='50%', direction=ui.ZoneDirection.COLUMN),
                        ui.zone('commands_top', size='50%'),
                    ],
                ),
                ui.zone(
                    'commands',
                    direction=ui.ZoneDirection.ROW,
                    justify=ui.ZoneJustify.BETWEEN,
                    align=ui.ZoneAlign.CENTER,
                ),
                ui.zone(
                    'content',
                    direction=ui.ZoneDirection.COLUMN,
                    justify=ui.ZoneJustify.START,
                    zones=[
                        ui.zone(
                            'main',
                            direction=ui.ZoneDirection.ROW,
                            justify=ui.ZoneJustify.START,
                            zones=[
                                ui.zone(
                                    'main_left',
                                    direction=ui.ZoneDirection.COLUMN,
                                    size='20%',
                                ),
                                ui.zone(
                                    'main_right',
                                    direction=ui.ZoneDirection.COLUMN,
                                    size='80%',
                                ),
                            ],
                        ),
                        ui.zone(
                            'main_center',
                            direction=ui.ZoneDirection.COLUMN,
                            justify=ui.ZoneJustify.BETWEEN,
                            align=ui.ZoneAlign.CENTER,
                        )
                    ],
                ),
                ui.zone('footer', direction=ui.ZoneDirection.ROW, justify=ui.ZoneJustify.CENTER),
            ],
        )
    ]
    return layouts
