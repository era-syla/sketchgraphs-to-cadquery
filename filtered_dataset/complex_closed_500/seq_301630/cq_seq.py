import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, -0.0055).lineTo(0.013, -0.0055).lineTo(0.013, -0.0155).lineTo(0.0, -0.0155).lineTo(0.0, -0.0055).close()
solid=wp_sketch0.add(loop0).extrude(0.035040683586338064)
