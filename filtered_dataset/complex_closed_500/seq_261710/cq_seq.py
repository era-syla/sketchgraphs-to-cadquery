import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.08).lineTo(-0.02574, 0.03542).lineTo(-0.07608, 0.02472).lineTo(-0.04164, -0.01353).lineTo(-0.04702, -0.06472).lineTo(-0.0, -0.04379).lineTo(0.04702, -0.06472).lineTo(0.04164, -0.01353).lineTo(0.07608, 0.02472).lineTo(0.02574, 0.03542).lineTo(-0.0, 0.08).close()
solid=wp_sketch0.add(loop0).extrude(-0.23896323461696783)
