import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00325, 0.008).lineTo(0.00325, 0.008).lineTo(0.00325, 0.0074).lineTo(-0.00325, 0.0074).lineTo(-0.00325, 0.008).close()
solid=wp_sketch0.add(loop0).extrude(0.017800539776184145)
