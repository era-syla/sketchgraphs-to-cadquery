import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0085, 0.026).lineTo(0.0085, 0.026).lineTo(0.0085, -0.004).lineTo(0.0135, -0.004).lineTo(0.0135, 0.031).lineTo(-0.0135, 0.031).lineTo(-0.0135, -0.004).lineTo(-0.0085, -0.004).lineTo(-0.0085, 0.026).close()
solid=wp_sketch0.add(loop0).extrude(0.022057913798572245)
