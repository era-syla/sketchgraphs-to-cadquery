import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0765, 0.02).lineTo(-0.0095, 0.02).lineTo(-0.0095, 0.002).lineTo(-0.0765, 0.002).lineTo(-0.0765, 0.02).close()
solid=wp_sketch0.add(loop0).extrude(0.15648908638705716)
