import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0381, 0.03334).lineTo(0.0381, 0.03334).lineTo(0.0381, -0.04286).lineTo(-0.0381, -0.04286).lineTo(-0.0381, 0.03334).close()
solid=wp_sketch0.add(loop0).extrude(0.0812805776867609)
