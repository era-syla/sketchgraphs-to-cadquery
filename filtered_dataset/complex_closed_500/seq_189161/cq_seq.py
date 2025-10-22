import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.07825, -0.00117).lineTo(-0.00275, -0.00117).lineTo(-0.00275, -0.04047).lineTo(-0.07825, -0.04047).lineTo(-0.07825, -0.00117).close()
solid=wp_sketch0.add(loop0).extrude(0.17030128842798942)
