import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04, 0.02682).lineTo(-0.047, 0.02682).lineTo(-0.047, 0.0302).lineTo(-0.05, 0.0302).lineTo(-0.05, 0.0258).lineTo(-0.049, 0.0248).lineTo(-0.041, 0.0248).lineTo(-0.04, 0.0258).lineTo(-0.04, 0.02682).close()
solid=wp_sketch0.add(loop0).extrude(-0.001570301618941832)
