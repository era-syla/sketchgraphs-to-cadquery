import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05, 0.0136).lineTo(0.05, 0.0136).lineTo(0.05, 0.0001).lineTo(-0.05, 0.0001).lineTo(-0.05, 0.0136).close()
solid=wp_sketch0.add(loop0).extrude(-0.007104257912044299)
