import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.15875, 0.0).lineTo(0.15875, 0.0).lineTo(0.09525, 0.28448).lineTo(-0.08255, 0.28448).lineTo(-0.15875, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.8227157814450736)
