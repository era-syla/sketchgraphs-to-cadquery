import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01809, 0.03098).lineTo(-0.09662, 0.03098).lineTo(-0.09662, -0.01979).lineTo(0.03195, -0.01979).lineTo(0.01809, 0.03098).close()
solid=wp_sketch0.add(loop0).extrude(-0.05583448560931235)
