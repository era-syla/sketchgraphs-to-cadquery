import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03853, -0.05985).lineTo(0.03956, -0.05985).lineTo(0.03956, 0.06653).lineTo(-0.03853, 0.06653).lineTo(-0.03853, -0.05985).close()
solid=wp_sketch0.add(loop0).extrude(0.11649100570629167)
