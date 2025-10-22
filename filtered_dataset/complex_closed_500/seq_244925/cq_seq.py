import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.04, 0.04204).lineTo(0.033, 0.04204).lineTo(0.033, 0.02904).lineTo(0.04, 0.02904).lineTo(0.04, 0.04204).close()
solid=wp_sketch0.add(loop0).extrude(0.008671150949119475)
