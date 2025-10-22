import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03062, 0.02774).lineTo(-0.00899, 0.02774).lineTo(-0.00899, 0.09976).lineTo(-0.03062, 0.09976).lineTo(-0.03062, 0.02774).close()
solid=wp_sketch0.add(loop0).extrude(0.15107127826247585)
