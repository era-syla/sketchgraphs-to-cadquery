import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.09695, -0.12956).lineTo(-0.16295, -0.08398).lineTo(-0.16295, -0.2326).lineTo(0.0, -0.2326).lineTo(-0.0, -0.09115).lineTo(-0.09695, -0.12956).close()
solid=wp_sketch0.add(loop0).extrude(0.09437032106446422)
