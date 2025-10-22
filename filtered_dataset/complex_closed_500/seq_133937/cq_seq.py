import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05646, 0.09373).lineTo(-0.08016, 0.07023).lineTo(-0.11157, 0.07563).lineTo(-0.10127, 0.13549).lineTo(-0.05646, 0.09373).close()
solid=wp_sketch0.add(loop0).extrude(-0.019175162077001696)
