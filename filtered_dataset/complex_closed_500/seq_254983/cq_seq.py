import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.03175).lineTo(-0.0275, -0.01588).lineTo(0.0275, -0.01588).lineTo(0.0, 0.03175).close()
solid=wp_sketch0.add(loop0).extrude(-0.04474828092678392)
