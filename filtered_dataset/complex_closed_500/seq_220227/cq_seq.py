import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-1.0414, 0.0).lineTo(-0.2794, 0.0).lineTo(-0.2794, 2.0574).lineTo(-1.0414, 2.0574).lineTo(-1.0414, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.19540547009532971)
