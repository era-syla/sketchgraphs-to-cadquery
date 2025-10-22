import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00165, 0.0).lineTo(0.00465, 0.0).lineTo(0.00465, 0.02139).lineTo(0.00165, 0.02139).lineTo(0.00165, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.060029205912848285)
