import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.049, -0.055).lineTo(-0.049, -0.055).lineTo(-0.049, 0.055).lineTo(0.049, 0.055).lineTo(0.049, -0.055).close()
solid=wp_sketch0.add(loop0).extrude(-0.3065430562596966)
