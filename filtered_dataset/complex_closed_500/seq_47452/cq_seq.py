import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.09525, 0.11113).lineTo(0.09525, -0.14923).lineTo(-0.09525, -0.14923).lineTo(-0.09525, 0.11113).lineTo(0.09525, 0.11113).close()
solid=wp_sketch0.add(loop0).extrude(-0.3337338109149427)
