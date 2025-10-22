import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.60642, 0.7366).lineTo(-0.60643, 0.7366).lineTo(-0.60643, 1.16205).lineTo(0.60642, 1.16205).lineTo(0.60642, 0.7366).close()
solid=wp_sketch0.add(loop0).extrude(-2.771330912566239)
