import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0035, 0.00202).lineTo(-0.0035, -0.00202).lineTo(-0.0, -0.00404).lineTo(0.0035, -0.00202).lineTo(0.0035, 0.00202).lineTo(-0.0, 0.00404).lineTo(-0.0035, 0.00202).close()
solid=wp_sketch0.add(loop0).extrude(0.020433613768106665)
