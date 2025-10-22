import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00358, 0.0213).lineTo(-0.00358, 0.01555).lineTo(-0.001, 0.01399).lineTo(-0.001, 0.0213).lineTo(-0.00358, 0.0213).close()
solid=wp_sketch0.add(loop0).extrude(0.021494141273139068)
