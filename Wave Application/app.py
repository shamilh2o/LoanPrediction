from h2o_wave import Q, app, handle_on, main

from common import make_base_ui, process_analysis, getPrediction


@app('/')
async def serve(q: Q):
    if q.args.clear_btn:
        await make_base_ui(q)
    elif q.args.submit_btn:
        await process_analysis(q)
    else:
        await make_base_ui(q)
    await q.page.save()
