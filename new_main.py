import new_core as nc

from rich import print

nc.InitialCheck()

try:
    nc.Loading()
    nc.Search.link_searcher(nc.link_of_interest)
    nc.sleep(10)
    nc.MouseController.scroll(-4)

    nc.sleep(3)
    nc.MouseController.scroll(-1)
    nc.sleep(1)
    nc.MouseController.pnt_clk(nc.mouse_psx,nc.mouse_psy)
    nc.sleep(10)

    nc.MouseController.pnt_clk(nc.screen_psx,nc.screen_psy)
    nc.Scraper()
    print('[bold red]Error, data not scraped.[/bold red]')

except KeyboardInterrupt:
    print('\n[green]Data Scraping Skipped[/green]\n')
    nc.sleep(2)

except:
    print('[bold red]Error, data not scraped.[/bold red]')

try:
    nc.Directory().directory()
    nc.sleep(1)
    nc.Directory().cropper()
    nc.AIPipeline().image_to_csv_pipeline()
    nc.Zipper()

except:
    print('[bold red]Error Occured[/bold red] either on Files, Cropper, AI Pipeline')