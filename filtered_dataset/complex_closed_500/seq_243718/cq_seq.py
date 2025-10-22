import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-2.07709, 0.1524).lineTo(5.92391, 0.1524).lineTo(5.92391, 0.0).lineTo(-2.07709, 0.0).lineTo(-2.07709, 0.1524).close()
solid=wp_sketch0.add(loop0).extrude(-14.610414962111264)
