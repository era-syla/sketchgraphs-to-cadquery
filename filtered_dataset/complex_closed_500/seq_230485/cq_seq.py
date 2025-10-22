import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04208, 0.02055).lineTo(-0.08272, 0.02055).lineTo(-0.08272, -0.0201).lineTo(-0.04208, -0.0201).lineTo(-0.04208, 0.02055).close()
solid=wp_sketch0.add(loop0).extrude(0.0959715442822208)
