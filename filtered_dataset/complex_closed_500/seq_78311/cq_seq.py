import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.008, -0.0646).lineTo(0.039, -0.0646).lineTo(0.039, -0.0536).lineTo(0.008, -0.0536).lineTo(0.008, -0.0646).close()
solid=wp_sketch0.add(loop0).extrude(-0.013186592622050316)
