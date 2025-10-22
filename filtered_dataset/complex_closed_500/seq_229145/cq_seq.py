import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.07548, 0.03972).lineTo(0.15452, 0.03972).lineTo(0.15452, -0.04028).lineTo(-0.07548, -0.04028).lineTo(-0.07548, 0.03972).close()
solid=wp_sketch0.add(loop0).extrude(0.3993415716060039)
