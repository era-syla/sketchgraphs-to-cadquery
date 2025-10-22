import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.125, 0.075).lineTo(0.125, 0.075).lineTo(0.125, -0.075).lineTo(-0.125, -0.075).lineTo(-0.125, -0.055).lineTo(-0.125, 0.055).lineTo(-0.135, 0.055).lineTo(-0.135, 0.075).lineTo(-0.125, 0.075).close()
solid=wp_sketch0.add(loop0).extrude(0.0026735357018272945)
