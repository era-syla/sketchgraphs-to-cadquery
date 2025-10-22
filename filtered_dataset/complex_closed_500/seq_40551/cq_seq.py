import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.04).lineTo(-0.0015, 0.04).lineTo(-0.0015, 0.028).lineTo(-0.0045, 0.028).lineTo(-0.0045, 0.026).lineTo(-0.0095, 0.026).lineTo(-0.014, 0.023).lineTo(-0.014, 0.005).lineTo(-0.013, 0.002).lineTo(-0.02, 0.002).lineTo(-0.02, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.04506208514085237)
