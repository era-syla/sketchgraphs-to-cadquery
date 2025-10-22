import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01769, 0.08089).lineTo(-0.01599, 0.08089).lineTo(-0.01599, 0.04283).lineTo(-0.01769, 0.04283).lineTo(-0.01769, 0.08089).close()
solid=wp_sketch0.add(loop0).extrude(0.04731029239836998)
