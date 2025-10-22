import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.06939, -0.05856).lineTo(0.07087, -0.05856).lineTo(0.07087, -0.10802).lineTo(-0.06939, -0.10802).lineTo(-0.06939, -0.05856).close()
solid=wp_sketch0.add(loop0).extrude(0.4176286939197739)
