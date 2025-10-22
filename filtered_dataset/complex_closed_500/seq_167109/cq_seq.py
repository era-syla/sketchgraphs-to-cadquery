import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.225, 0.64).lineTo(-0.225, 0.64).lineTo(-0.225, -0.64).lineTo(0.225, -0.64).lineTo(0.225, 0.19).lineTo(0.825, 0.19).lineTo(0.825, 0.64).lineTo(0.225, 0.64).close()
solid=wp_sketch0.add(loop0).extrude(-1.8869440881432502)
