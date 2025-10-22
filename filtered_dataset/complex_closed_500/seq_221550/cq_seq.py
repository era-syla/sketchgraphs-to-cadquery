import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.6096, 0.762).lineTo(0.6096, 0.762).lineTo(0.6096, 0.2667).lineTo(-0.6096, 0.2667).lineTo(-0.6096, 0.762).close()
solid=wp_sketch0.add(loop0).extrude(3.644129667730201)
