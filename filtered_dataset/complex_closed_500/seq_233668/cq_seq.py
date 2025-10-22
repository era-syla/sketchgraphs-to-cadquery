import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02757, 0.04075).lineTo(0.02758, 0.04075).lineTo(0.02757, -0.04075).lineTo(-0.02758, -0.04075).lineTo(-0.02757, 0.04075).close()
solid=wp_sketch0.add(loop0).extrude(-0.07056969046868444)
