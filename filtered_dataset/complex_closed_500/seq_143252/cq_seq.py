import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01, -1.3294).lineTo(-0.51, -1.3294).lineTo(-0.51, -0.0294).lineTo(-0.01, -0.0294).lineTo(-0.01, -1.3294).close()
solid=wp_sketch0.add(loop0).extrude(1.7143816538509797)
