import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.09144).lineTo(0.0, 0.08768).lineTo(-0.02934, 0.08768).lineTo(-0.02934, 0.09144).lineTo(0.0, 0.09144).close()
solid=wp_sketch0.add(loop0).extrude(-0.07800950615650917)
