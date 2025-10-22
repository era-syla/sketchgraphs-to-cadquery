import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.29994, -0.48162).lineTo(-0.07668, -0.49986).lineTo(-0.07684, -0.50185).lineTo(-0.3001, -0.48362).lineTo(-0.29994, -0.48162).close()
solid=wp_sketch0.add(loop0).extrude(-0.19253126919348706)
