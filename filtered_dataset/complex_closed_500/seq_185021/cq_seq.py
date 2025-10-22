import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.047, 0.014).lineTo(-0.029, -0.01).lineTo(-0.037, -0.016).lineTo(-0.055, 0.008).lineTo(-0.047, 0.014).close()
solid=wp_sketch0.add(loop0).extrude(0.007833849913787239)
