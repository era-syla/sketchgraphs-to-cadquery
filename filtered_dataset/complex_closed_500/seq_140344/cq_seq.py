import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.08, -0.01392).lineTo(-0.095, -0.01392).lineTo(-0.095, 0.01392).lineTo(-0.08, 0.01392).lineTo(-0.08, -0.01392).close()
solid=wp_sketch0.add(loop0).extrude(0.07866677104570108)
