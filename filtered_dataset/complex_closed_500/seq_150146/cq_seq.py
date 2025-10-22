import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.10795, 0.33655).lineTo(0.10795, 0.33655).lineTo(0.10795, 0.01905).lineTo(-0.10795, 0.01905).lineTo(-0.10795, 0.33655).close()
solid=wp_sketch0.add(loop0).extrude(0.2452736075181664)
