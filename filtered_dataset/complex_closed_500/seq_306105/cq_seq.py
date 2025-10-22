import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.04, 0.0275).lineTo(-0.04, 0.0275).lineTo(-0.04, -0.0275).lineTo(0.04, -0.0275).lineTo(0.04, 0.0275).close()
solid=wp_sketch0.add(loop0).extrude(0.23051564366304653)
