import os

from h2o_wave import ui

from layouts import get_layouts
from wave_utils import WaveColors


def get_meta(theme):
    tracker_id = os.environ.get('TRACKER_ID', "")
    return ui.meta_card(
        box='',
        title="Home Loan",
        layouts=get_layouts(),
        tracker=ui.tracker(type=ui.TrackerType.GA, id=tracker_id),
        themes=[
            ui.theme(
                name='MCAC-Dark',
                primary=WaveColors.h2o,
                text=WaveColors.white,
                card=WaveColors.light_gray,
                page=WaveColors.black,
            )
        ],
        theme=theme,
    )


def get_header():
    return ui.header_card(
        box=ui.box('header'),
        title="Home Loan Application",
        subtitle="Check whether you are eligible to have a house loan",
        icon='Home',
        icon_color='#000000',
    )


def get_user_input_form():
    items = [
        ui.textbox(name='total_income', label='Total Income (In thousands)', required=True),
        ui.textbox(name='loan_amount', label='Loan Amount (In Thousands)', required=True),
        ui.textbox(name='loan_terms', label='Loan Terms (In Months)', required=True),
        ui.textbox(name='credit_history', label='Credit History (1: Records Available, 0: Records Unavailable)', required=True),
        ui.dropdown(name='gender', label='Gender', required=True, choices=[ui.choice('male', 'Male'), ui.choice('female', 'Female')]),
        ui.dropdown(name='status', label='Status', required=True, choices=[ui.choice('married', 'Married'), ui.choice('single', 'Single')]),
        ui.dropdown(name='dependents', label='Dependents', required=True, choices=[ui.choice('0', '0'), ui.choice('1', '1'), ui.choice('2', '2'), ui.choice('3', '3 or More')]),
        ui.dropdown(name='graduated', label='Graduated', required=True, choices=[ui.choice('yes', 'Yes'), ui.choice('no', 'No')]),
        ui.dropdown(name='employment', label='Self Employee', required=True, choices=[ui.choice('yes', 'Yes'), ui.choice('no', 'No')]),
        ui.dropdown(name='area', label='Property Area', required=True, choices=[ui.choice('rural', 'Rural'), ui.choice('semi_urban', 'Semi Urban'), ui.choice('urban', 'Urban')]),
        ui.buttons(
            items=[
                ui.button(
                    name="submit_btn",
                    label="Submit",
                    icon="Upload",
                    primary=True,
                ),
                ui.button(
                    name="clear_btn",
                    label="Clear",
                    icon="Clear",
                )
            ],
            justify=ui.ButtonsJustify.END
        )
    ]

    return ui.form_card(
        box=ui.box('commands'),
        items=items
    )


def get_footer():
    return ui.footer_card(
        box=ui.box('footer', order=1, width="475px"),
        caption='<p style="text-align: center;">Made with 💛️ using <a href="https://h2oai.github.io/wave/", target="_blank">Wave</a>. (c) 2021 H2O.ai. All rights reserved.</p>' # noqa: E501
    )


def get_status(status, state):
    if state == 1:
        return ui.form_card(box='main_center', items=[ui.text_l(status)])
    elif state == 2:
        return ui.form_card(box='main_center', items=[ui.text_l(status)])
    else:
        return ui.form_card(box='main_center', items=[ui.text(status)])
