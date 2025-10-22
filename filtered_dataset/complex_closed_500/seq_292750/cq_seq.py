import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.07627, 0.04932).lineTo(-0.05395, 0.04932).lineTo(-0.05395, 0.02974).lineTo(-0.07627, 0.02974).lineTo(-0.07627, 0.04932).close()
solid=wp_sketch0.add(loop0).extrude(0.04429957933013117)
