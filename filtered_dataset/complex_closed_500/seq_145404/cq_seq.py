import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01685, 0.0).lineTo(0.02515, 0.0).lineTo(0.02515, 0.01).lineTo(-0.01685, 0.01).lineTo(-0.01685, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.06923436958888614)
