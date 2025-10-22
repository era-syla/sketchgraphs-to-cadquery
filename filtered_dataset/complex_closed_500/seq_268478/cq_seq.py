import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.12772, -0.08025).lineTo(0.12772, -0.02173).lineTo(-0.12488, 0.14492).lineTo(-0.12488, 0.03542).lineTo(-0.0135, -0.0395).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.40416215531742944)
