import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0762, 0.00073).lineTo(0.0762, 0.10233).lineTo(0.0, 0.10233).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.16119855611425626)
