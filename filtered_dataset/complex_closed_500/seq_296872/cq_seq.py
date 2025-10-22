import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0033, 0.01746).lineTo(-0.0033, 0.01746).lineTo(-0.0033, -0.01746).lineTo(-0.0073, -0.01746).lineTo(-0.0073, 0.02146).lineTo(0.0073, 0.02146).lineTo(0.0073, -0.01746).lineTo(0.0033, -0.01746).lineTo(0.0033, 0.01746).close()
solid=wp_sketch0.add(loop0).extrude(0.012400885298882875)
