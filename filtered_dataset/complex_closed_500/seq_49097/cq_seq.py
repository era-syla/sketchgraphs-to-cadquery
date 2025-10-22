import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.09713, -0.02631).lineTo(-0.06739, 0.02686).lineTo(-0.04069, 0.01722).lineTo(-0.04208, 0.01336).lineTo(-0.09713, -0.02631).close()
solid=wp_sketch0.add(loop0).extrude(-0.010168828128155333)
